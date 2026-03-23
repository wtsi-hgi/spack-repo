import os
import shutil
from textwrap import dedent

from spack.package import *


class Ggnc(Package):
    """Global Genomic Network Communities (GG-NC) pipeline and Shiny browser
    for exploring genomic network communities. Upstream distributes a Docker
    image; this package provides the same scripts directly on Singularity /
    Spack environments."""

    homepage = "https://github.com/mariajpalma/GG-NC"
    git = "https://github.com/mariajpalma/GG-NC.git"

    maintainers("softpack")
    license("Apache-2.0")

    version("20260224", commit="50e03e6c84e71c0db97d968749170b671257308a")

    depends_on("r@4.4.1:", type=("build", "run"))
    depends_on("r-aricode@1.0.3:", type="run")
    depends_on("r-bslib@0.7.0:", type="run")
    depends_on("r-chameleon@0.2-3:", type="run")
    depends_on("r-circlize@0.4.16:", type="run")
    depends_on("r-complexheatmap@2.18.0:", type="run")
    depends_on("r-data-table@1.15.4:", type="run")
    depends_on("r-desctools@0.99.54:", type="run")
    depends_on("r-doparallel@1.0.17:", type="run")
    depends_on("r-dplyr@1.1.4:", type="run")
    depends_on("r-foreach@1.5.2:", type="run")
    depends_on("r-ggplot2@3.5.2:", type="run")
    depends_on("r-igraph@2.0.3:", type="run")
    depends_on("r-iterators@1.0.14:", type="run")
    depends_on("r-leaflet@2.2.1:", type="run")
    depends_on("r-leaflet-minicharts@0.6.2:", type="run")
    depends_on("r-matrix@1.6.5:", type="run")
    depends_on("r-plotly@4.10.4:", type="run")
    depends_on("r-pracma@2.4.4:", type="run")
    depends_on("r-pryr@0.1.6:", type="run")
    depends_on("r-rgl@1.3.1:", type="run")
    depends_on("r-shiny@1.8.0:", type="run")
    depends_on("r-shinyalert@3.0.0:", type="run")
    depends_on("r-shinybs@0.61.1:", type="run")
    depends_on("r-shinybusy@0.3.3:", type="run")
    depends_on("r-shinyscreenshot@0.2.1:", type="run")
    depends_on("r-shinytitle@0.1.0:", type="run")
    depends_on("r-shinywidgets@0.8.3:", type="run")
    depends_on("r-ucie@1.0.2:", type="run")
    depends_on("r-viridis@0.6.5:", type="run")
    depends_on("r-viridislite@0.4.2:", type="run")
    depends_on("r-vembedr@0.1.5:", type="run")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-matplotlib@3.8:", type=("build", "run"))
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-scipy@1.12:", type=("build", "run"))
    depends_on("py-seaborn@0.13:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("tskit@0.3:", type=("build", "run"))

    def install(self, spec, prefix):
        ggnc_home = join_path(prefix.share, "ggnc")
        source_path = self.stage.source_path
        for extra in (".git", ".github"):
            candidate = join_path(source_path, extra)
            if os.path.isdir(candidate):
                shutil.rmtree(candidate)
            elif os.path.isfile(candidate):
                os.remove(candidate)

        install_tree(source_path, ggnc_home)

        main_script = join_path(ggnc_home, "Parameters_GGNC_v2.sh")
        if not os.path.exists(main_script):
            raise InstallError("Parameters_GGNC_v2.sh missing from upstream source")

        tmrca_script = join_path(ggnc_home, "Aux_scripts", "TMRCA_csvpair.py")
        violin_script = join_path(ggnc_home, "tmrcas_violin_sampling.py")
        python_cli = spec["python"].command.path
        demo_dir = join_path(ggnc_home, "demos")

        mkdirp(prefix.bin)
        wrappers = {
            "ggnc-run": dedent(
                f"""\
                #!/bin/bash
                set -euo pipefail
                export GGNC_HOME="{ggnc_home}"
                export GGNC_DEMOS="{demo_dir}"
                export PYTHON_BIN="{python_cli}"

                case "${{1:-}}" in
                    --print-home)
                        printf '%s\\n' "$GGNC_HOME"
                        exit 0
                        ;;
                    -h|--help)
                        cat <<'EOF'
                Usage:
                  ggnc-run -k <metric> -p <data_dir> -d <data> -i <info> [options]

                This command executes Parameters_GGNC_v2.sh from the upstream
                GG-NC Docker image. Demo inputs are available under:
                  $GGNC_DEMOS/Input
                Refer to README.md in $GGNC_HOME for the full flag reference.
                EOF
                        exit 0
                        ;;
                esac

                exec bash "{main_script}" "$@"
                """
            ),
            "ggnc-tmrca-csvpair": dedent(
                f"""\
                #!/bin/bash
                set -euo pipefail
                export GGNC_HOME="{ggnc_home}"
                exec "{python_cli}" "{tmrca_script}" "$@"
                """
            ),
            "ggnc-tmrca-violin": dedent(
                f"""\
                #!/bin/bash
                set -euo pipefail
                export GGNC_HOME="{ggnc_home}"
                exec "{python_cli}" "{violin_script}" "$@"
                """
            ),
        }

        for name, content in wrappers.items():
            wrapper_path = join_path(prefix.bin, name)
            with open(wrapper_path, "w", encoding="utf-8") as fout:
                fout.write(content)
            set_executable(wrapper_path)

    def setup_run_environment(self, env):
        ggnc_home = join_path(self.prefix.share, "ggnc")
        env.set("GGNC_HOME", ggnc_home)
        env.set("GGNC_DEMOS", join_path(ggnc_home, "demos"))
        env.prepend_path("PATH", self.prefix.bin)

    @run_after("install")
    def install_test(self):
        ggnc_run = Executable(join_path(self.prefix.bin, "ggnc-run"))
        tmrca_wrapper = Executable(join_path(self.prefix.bin, "ggnc-tmrca-violin"))
        with working_dir("spack-test", create=True):
            ggnc_run("--print-home")
            ggnc_run("--help")
            tmrca_wrapper("--help")
