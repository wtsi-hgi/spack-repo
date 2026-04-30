# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySqanti3(Package):
    """SQANTI3 will continue as an integrated development aiming to provide the best characterization for your new long read-defined transcriptome."""

    homepage = "https://github.com/ConesaLab/SQANTI3"
    url = "https://github.com/ConesaLab/SQANTI3/archive/refs/tags/v5.3.0.tar.gz"
    git = "https://github.com/ConesaLab/SQANTI3.git"

    license("GPL-3.0")

    version("6.0.1", tag="v6.0.1")
    version("6.0.0", tag="v6.0")
    version("5.3.0", tag="v5.3.0")

    with default_args(type=("build", "run")):
        depends_on("python@3.7:3.11")
        depends_on("py-argcomplete")
        depends_on("py-bcbio-gff")
        depends_on("py-bx-python")
        depends_on("py-cython")
        depends_on("gffread")
        depends_on("py-jinja2")
        depends_on("kallisto")
        depends_on("minimap2")
        depends_on("py-numpy@1.26:1")
        depends_on("openssl")
        depends_on("py-pandas")
        depends_on("pandoc")
        depends_on("perl")
        depends_on("py-psutil")
        depends_on("py-pybedtools")
        depends_on("py-pysam")
        depends_on("r-biocmanager")
        depends_on("r-caret")
        depends_on("r-dplyr")
        depends_on("r-dt")
        depends_on("r-devtools")
        depends_on("r-e1071")
        depends_on("r-forcats")
        depends_on("r-ggplotify")
        depends_on("r-gridbase")
        depends_on("r-gridextra")
        depends_on("r-htmltools")
        depends_on("r-jsonlite")
        depends_on("r-optparse")
        depends_on("r-plotly")
        depends_on("r-plyr")
        depends_on("r-purrr")
        depends_on("r-rmarkdown")
        depends_on("r-reshape")
        depends_on("r-readr")
        depends_on("r-scales")
        depends_on("r-stringi")
        depends_on("r-stringr")
        depends_on("r-tibble")
        depends_on("r-tidyr")
        depends_on("r-noiseq")
        depends_on("r-busparse")
        depends_on("samtools")
        depends_on("seqtk")
        depends_on("star")
        depends_on("py-seaborn")
        depends_on("py-scikit-learn")
        depends_on("py-pdf2image")
        depends_on("py-biopython")
        depends_on("gmap-gsnap")
        depends_on("r-ggplot2")
        depends_on("r-proc")
        depends_on("r-randomforest")
        depends_on("py-scipy@:1.11.4")
        depends_on("py-ultra-bioinformatics")
        depends_on("py-gtftools")
        depends_on("desalt")
        depends_on("slamem")
        depends_on("curl")

        with when("@6:"):
            depends_on("python@3.11")
            depends_on("py-pyyaml@6.0.3")
            depends_on("py-scipy@:1.11")
            depends_on("py-pandas@2.2")
            depends_on("py-scikit-learn@1.5")
            depends_on("py-seaborn@0.13")
            depends_on("py-argcomplete@3.4:")
            depends_on("py-cython@3.0:")
            depends_on("py-jinja2@3.1:")
            depends_on("py-psutil@6.1:")
            depends_on("py-pip@24:")

            depends_on("py-bcbio-gff@0.7:")
            depends_on("py-biopython@1.81")
            depends_on("py-bx-python@0.11:")
            depends_on("gffread@0.12:")
            depends_on("py-gtftools@0.9:")
            depends_on("namfinder@0.13:")
            depends_on("py-pysam@0.22")
            depends_on("samtools@1.21:")
            depends_on("desalt@1.5:")
            depends_on("kallisto@0.48:")

            depends_on("minimap2@2.28")
            depends_on("star@2.7.11b")

            depends_on("r@4.3.3:")
            depends_on("r-biocmanager@1.30:")
            depends_on("r-caret@6.0:")
            depends_on("r-dplyr@1.1:")
            depends_on("r-dt@0.33:")
            depends_on("r-devtools@2.4:")
            depends_on("r-e1071@1.7:")
            depends_on("r-forcats@1.0:")
            depends_on("r-ggplot2@3.4.0:")
            depends_on("r-ggplotify@0.1:")
            depends_on("r-gridbase@0.4:")
            depends_on("r-gridextra@2.3:")

            depends_on("r-htmltools@0.5:")
            depends_on("r-jsonlite@1.8:")
            depends_on("r-optparse@1.7:")
            depends_on("r-plotly@4.10:")
            depends_on("r-plyr@1.8:")
            depends_on("r-purrr@1.0:")
            depends_on("r-rmarkdown@4.7:")
            depends_on("r-reshape@0.8:")
            depends_on("r-readr@2.1:")
            depends_on("r-scales@1.3:")
            depends_on("r-stringi@1.8:")
            depends_on("r-stringr@1.5:")
            depends_on("r-tibble@3.2:")
            depends_on("r-tidyr@1.3:")
            depends_on("r-noiseq@2.46:")
            depends_on("r-gviz")
            depends_on("openssl@3.4:")
            depends_on("pandoc@3.5:")
            depends_on("perl@5.32")

            depends_on("py-argh@0.31:")
            depends_on("py-dill@0.3.9:")
            depends_on("py-edlib@1.3.9:")
            depends_on("py-gffutils@0.13:")
            depends_on("py-gtfparse@2.5:")
            depends_on("py-importlib-metadata@8.5:")
            depends_on("py-intervaltree@3.1:")
            depends_on("py-parasail@1.3:")
            depends_on("py-pdf2image@1.17:")
            depends_on("py-polars@0.20")
            depends_on("py-pyarrow@14")
            depends_on("py-pyfaidx@0.8:")
            depends_on("py-simplejson@3.19:")
            depends_on("py-sortedcontainers@2.4:")
            depends_on("py-ultra-bioinformatics@0.1:")
            depends_on("py-zipp@3.21:")
            depends_on("py-td2@1.0:")





    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["curl"].prefix.lib)

    def install(self, sepc, prefix):
        install_tree(".", prefix.bin)
    
    @run_after("install")
    def install_test(self):
        Executable(join_path(self.prefix.bin, "sqanti3"))()
