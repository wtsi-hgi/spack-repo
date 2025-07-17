# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse13015(RPackage):
    """GEO accession data GSE13015_GPL6106 as a SummarizedExperiment

    Microarray expression matrix platform GPL6106 and clinical data for 67 septicemic patients and made them available as GEO accession [GSE13015](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE13015). GSE13015 data have been parsed into a SummarizedExperiment object available in ExperimentHub. This data data could be used as an example supporting BloodGen3Module R package.
    """

    bioc = "GSE13015"

    version("1.16.0", commit="a888b4b08ce3e219eb0319d6d7b7d4ed5012beaa")
    version("1.10.0", commit="b7f36ac8cc10bf1da0a4afb362c41c569ee3fa33")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
