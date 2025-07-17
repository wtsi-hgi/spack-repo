# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmite(RPackage):
    """Significance-based Modules Integrating the Transcriptome and Epigenome

    This package builds on the Epimods framework which facilitates finding weighted subnetworks ("modules") on Illumina Infinium 27k arrays using the SpinGlass algorithm, as implemented in the iGraph package. We have created a class of gene centric annotations associated with p-values and effect sizes and scores from any researchers prior statistical results to find functional modules.
    """

    homepage = "https://github.com/GreallyLab/SMITE"
    bioc = "SMITE"

    version("1.36.0", commit="893b091e2d7d099ece9560b78682a1981e372b61")
    version("1.30.0", commit="7e7699a694ad0ea8cc4ec2c531160624805b556f")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-org-hs-eg-db", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reactome-db", type=("build", "run"))
    depends_on("r-keggrest", type=("build", "run"))
    depends_on("r-bionet", type=("build", "run"))
    depends_on("r-goseq", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genelendatabase", type=("build", "run"))
