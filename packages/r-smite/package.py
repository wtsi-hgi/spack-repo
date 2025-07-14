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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SMITE_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SMITE/SMITE_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="4dd237f2511774db0c583430ba205548df21ccf077f3dae0d0810ec29de4e043")

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
