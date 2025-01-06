# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-sqanti3
#
# You can edit this file again by typing:
#
#     spack edit py-sqanti3
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySqanti3(BundlePackage):
    """SQANTI3 will continue as an integrated development aiming to provide the best characterization for your new long read-defined transcriptome."""

    homepage = "https://github.com/ConesaLab/SQANTI3"
    url = "https://github.com/ConesaLab/SQANTI3/archive/refs/tags/v5.3.0.tar.gz"

    license("GPL-3.0")

    version("5.3.0")

    depends_on("python@3.7:3.11", type=("build", "run"))
    depends_on("py-argcomplete", type=("build", "run"))
    depends_on("py-bcbio-gff", type=("build", "run"))
    depends_on("py-bx-python", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("gffread", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("kallisto", type=("build", "run"))
    depends_on("minimap2", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("openssl", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("pandoc", type=("build", "run"))
    depends_on("perl", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-ggplotify", type=("build", "run"))
    depends_on("r-gridbase", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-optparse", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-noiseq", type=("build", "run"))
    depends_on("r-busparse", type=("build", "run"))
    depends_on("samtools", type=("build", "run"))
    depends_on("seqtk", type=("build", "run"))
    depends_on("star", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-pdf2image", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("gmap-gsnap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-ultra-bioinformatics", type=("build", "run"))
    depends_on("py-gtftools", type=("build", "run"))
    depends_on("desalt", type=("build", "run"))
    depends_on("slamem", type=("build", "run"))
    depends_on("curl", type=("build", "run", "link"))
