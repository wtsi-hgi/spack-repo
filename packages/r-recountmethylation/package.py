# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecountmethylation(RPackage):
    """Access and analyze public DNA methylation array data compilations

    Resources for cross-study analyses of public DNAm array data from NCBI GEO repo, produced using Illumina's Infinium HumanMethylation450K (HM450K) and MethylationEPIC (EPIC) platforms. Provided functions enable download, summary, and filtering of large compilation files. Vignettes detail background about file formats, example analyses, and more. Note the disclaimer on package load and consult the main manuscripts for further info.
    """

    homepage = "https://github.com/metamaden/recountmethylation"
    bioc = "recountmethylation"

    version("1.18.0", commit="cb06ac68a63bb403d260facc65c8f94e08d6a18a")
    version("1.12.0", commit="ac970f5573806232931f119ee597900e36a0b4b0")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-minfi", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
