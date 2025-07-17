# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbaf(RPackage):
    """Automated functions for comparing various omic data from cbioportal.org

    This package contains functions that allow analysing and comparing omic data across various cancers/cancer subgroups easily. So far, it is compatible with RNA-seq, microRNA-seq, microarray and methylation datasets that are stored on cbioportal.org.
    """

    bioc = "cbaf"

    version("1.30.0", commit="cfa9978e77cd36969d35c2c5da309d86e9d1ab7f")
    version("1.24.0", commit="e7d2904355c751af6a888ada06cc5630483468ee")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-cbioportaldata", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-openxlsx", type=("build", "run"))
