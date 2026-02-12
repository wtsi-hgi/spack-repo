# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack.package import *


class Gridss(Package):
    """GRIDSS: the Genomic Rearrangement IDentification Software Suite."""

    homepage = "https://github.com/PapenfussLab/gridss"
    url      = "https://github.com/PapenfussLab/gridss/releases/download/v2.13.2/gridss-2.13.2.tar.gz"

    license("GPL-3.0-only")

    version("2.13.2", sha256="4d5651b1fc27928c0f76f1e8e7b90a74e6feae0c1cb9abea17fa2bd359f1d704")

    depends_on("java@8:", type=("build", "run"))
    depends_on("curl", type=("build", "run"))
    depends_on("zlib", type=("build", "run"))
    depends_on("bzip2", type=("build", "run"))
    depends_on("xz", type=("build", "run"))
    depends_on("zstd", type=("build", "run"))
    depends_on("bwa", type="run")
    depends_on("samtools", type="run")
    depends_on("bcftools", type="run")
    depends_on("kraken2", type="run")
    depends_on("repeatmasker", type="run")
    depends_on("libdeflate", type=("run", "link"))
    depends_on("openssl@1.1.1:1.1", type=("run", "link"))

    # R dependencies for GRIDSS scripts
    depends_on("r@3.5:", type="run")
    depends_on("r-biocgenerics", type="run")
    depends_on("r-s4vectors", type="run")
    depends_on("r-iranges", type="run")
    depends_on("r-matrixstats", type="run")
    depends_on("r-delayedarray", type="run")
    depends_on("r-xvector", type="run")
    depends_on("r-biostrings", type="run")
    depends_on("r-biobase", type="run")
    depends_on("r-variantannotation", type="run")
    depends_on("r-rtracklayer", type="run")
    depends_on("r-structuralvariantannotation", type="run")
    depends_on("r-tidyverse", type="run")
    depends_on("r-stringr", type="run")
    depends_on("r-testthat", type="run")
    depends_on("r-stringdist", type="run")
    depends_on("r-argparser", type="run")
    depends_on("r-readr", type="run")
    depends_on("r-ggplot2", type="run")

    def install(self, spec, prefix):
        if os.path.exists("virusbreakend"):
            # Guard virusbreakend trap from nounset failures when --help exits early.
            filter_file(
                'current_command=""',
                'current_command=""\nlogfile=/dev/null',
                "virusbreakend",
                string=True,
            )

        mkdirp(prefix.bin)
        gridss_share = join_path(prefix.share, "gridss")
        mkdirp(gridss_share)

        jar_file = self._locate_release_jar()
        install(jar_file, gridss_share)
        jar_src = join_path(gridss_share, os.path.basename(jar_file))
        jar_dst = join_path(gridss_share, self._jar_basename())
        if os.path.basename(jar_file) != self._jar_basename():
            os.rename(jar_src, jar_dst)

        required_scripts = {"gridss", "virusbreakend"}
        scripts = [
            "gridss",
            "virusbreakend",
            "virusbreakend-build",
            "gridss_annotate_vcf_kraken2",
            "gridss_annotate_vcf_repeatmasker",
            "gridss_extract_overlapping_fragments",
            "gridss_somatic_filter",
            "gridsstools",
        ]
        for script in scripts:
            if not os.path.exists(script):
                if script in required_scripts:
                    raise InstallError("Required helper '{}' missing from release archive".format(script))
                continue
            install(script, prefix.bin)
            os.chmod(join_path(prefix.bin, script), 0o755)

        for rfile in ["libgridss.R", "gridss.config.R"]:
            if os.path.exists(rfile):
                install(rfile, prefix.bin)

    def setup_run_environment(self, env):
        jar_path = join_path(self.prefix.share, "gridss", self._jar_basename())
        env.set("GRIDSS_JAR", jar_path)
        env.prepend_path("PATH", self.prefix.bin)

        for lib_path in self._runtime_library_paths():
            env.prepend_path("LD_LIBRARY_PATH", lib_path)

    @run_after("install")
    def install_test(self):
        test_env = os.environ.copy()
        lib_paths = self._runtime_library_paths()
        if lib_paths:
            ld_path = test_env.get("LD_LIBRARY_PATH", "")
            test_env["LD_LIBRARY_PATH"] = os.pathsep.join(lib_paths + ([ld_path] if ld_path else []))

        virusbreakend = Executable(join_path(self.prefix.bin, "virusbreakend"))
        gridsstools = Executable(join_path(self.prefix.bin, "gridsstools"))
        with working_dir("spack-test", create=True):
            virusbreakend("--help", env=test_env)
            gridsstools("--version", env=test_env)

    def _jar_basename(self):
        return "gridss-{0}-gridss-jar-with-dependencies.jar".format(self.version)

    def _locate_release_jar(self):
        expected = self._jar_basename()
        if os.path.exists(expected):
            return expected
        jar_candidates = glob.glob("gridss-*-gridss-jar-with-dependencies.jar")
        if not jar_candidates:
            raise InstallError("GRIDSS release jar not found in source archive")
        return jar_candidates[0]

    def _runtime_library_paths(self):
        lib_names = ("libdeflate", "openssl", "curl", "zlib", "bzip2", "xz", "zstd")
        paths = []
        for name in lib_names:
            if name in self.spec:
                for directory in self.spec[name].libs.directories:
                    if directory not in paths:
                        paths.append(directory)
        return paths
