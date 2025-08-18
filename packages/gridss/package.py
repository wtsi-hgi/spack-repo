# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import glob


class Gridss(Package):
    """GRIDSS: the Genomic Rearrangement IDentification Software Suite."""

    homepage = "https://github.com/PapenfussLab/gridss"
    url      = "https://github.com/PapenfussLab/gridss/releases/download/v2.13.2/gridss-2.13.2.tar.gz"

    license("GPL-3.0-only")

    # Latest release asset containing prebuilt jar and scripts
    version("2.13.2", sha256="4d5651b1fc27928c0f76f1e8e7b90a74e6feae0c1cb9abea17fa2bd359f1d704")

    depends_on("java@8:", type=("build", "run"))
    depends_on("bwa", type="run")
    depends_on("samtools", type="run")
    depends_on("bcftools", type="run")
    depends_on("kraken2", type="run")
    depends_on("repeatmasker", type="run")
    depends_on("libdeflate", type=("run", "link"))
    depends_on("openssl", type=("run", "link"))
    
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
        # Create installation directories
        mkdir(prefix.bin)
        mkdir(prefix.share)
        gridss_share = join_path(prefix.share, "gridss")
        mkdir(gridss_share)

        # Install the prebuilt jar from the release asset
        jar_candidates = glob.glob("gridss-*-gridss-jar-with-dependencies.jar")
        if not jar_candidates:
            raise InstallError("GRIDSS release jar not found in source archive")
        jar_file = jar_candidates[0]
        install(jar_file, gridss_share)

        # Install provided scripts and utilities as-is (no wrappers)
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
            if os.path.exists(script):
                install(script, prefix.bin)
                os.chmod(join_path(prefix.bin, script), 0o755)

        # Install R support files alongside scripts so defaults work out-of-the-box
        for rfile in ["libgridss.R", "gridss.config.R"]:
            if os.path.exists(rfile):
                install(rfile, prefix.bin)

    def setup_run_environment(self, env):
        # Allow running scripts without specifying -j/--jar by exporting GRIDSS_JAR
        jar_name = "gridss-{}-gridss-jar-with-dependencies.jar".format(self.version)
        env.set("GRIDSS_JAR", join_path(self.prefix.share, "gridss", jar_name))
        env.prepend_path("PATH", self.prefix.bin)
        
        # Add library paths for shared libraries required by gridsstools
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libdeflate"].libs.directories[0])
        env.prepend_path("LD_LIBRARY_PATH", self.spec["openssl"].libs.directories[0])