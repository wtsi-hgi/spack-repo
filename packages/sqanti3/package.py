from spack.package import *


class Sqanti3(Package):
    """Structural and Quality Annotation of Novel Transcript Isoforms."""

    homepage = "https://github.com/ConesaLab/SQANTI3"
    url = "https://github.com/ConesaLab/SQANTI3/archive/refs/tags/v6.0.tar.gz"
    git = "https://github.com/ConesaLab/SQANTI3.git"

    version("6.0", sha256="7703da9acca51150d4e1ab9def8bf1cd37e507a760a9a5259b9cd9b8be1fd3fa")

    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-pyyaml", type=("run"))

    def install(self, spec, prefix):
        install_tree(".", prefix)

        mkdirp(prefix.bin)
        install("sqanti3", prefix.bin)
        install("sqanti3_qc.py", prefix.bin)
        install("sqanti3_filter.py", prefix.bin)
        install("sqanti3_rescue.py", prefix.bin)
        install("sqanti3_reads.py", prefix.bin)

        for script in ["sqanti3", "sqanti3_qc.py", "sqanti3_filter.py", "sqanti3_rescue.py", "sqanti3_reads.py"]:
            filter_file(
                "^#!/usr/bin/env python$",
                "#!/usr/bin/env python\nimport os\nimport sys\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))",
                join_path(prefix.bin, script),
                string=True,
            )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import sys; sys.path.insert(0, '{0}'); import src.wrapper_utils; print(src.wrapper_utils.__name__)".format(self.prefix))
