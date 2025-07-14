# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunotation(RPackage):
	"""Tools for working with diverse immune genes

	MHC (major histocompatibility complex) molecules are cell surface complexes that present antigens to T cells.  The repertoire of antigens presented in a given genetic background largely depends on the sequence of the encoded MHC molecules, and thus, in humans, on the highly variable HLA (human leukocyte antigen) genes of the hyperpolymorphic HLA locus. More than 28,000 different HLA alleles have been reported, with significant differences in allele frequencies between human populations worldwide. Reproducible and consistent annotation of HLA alleles in large-scale bioinformatics workflows remains challenging, because the available reference databases and software tools often use different HLA naming schemes. The package immunotation provides tools for consistent annotation of HLA genes in typical immunoinformatics workflows such as for example the prediction of MHC-presented peptides in different human donors. Converter functions that provide mappings between different HLA naming schemes are based on the MHC restriction ontology (MRO). The package also provides automated access to HLA alleles frequencies in worldwide human reference populations stored in the Allele Frequency Net Database.
	"""
	
	bioc = "immunotation"

	version("1.16.0", commit="f389cfcd3cb893ee5d67a65e6e00650f4ec82a5a")
	version("1.10.0", commit="a307830d088d82c9050092571599cf88dfcb1c24")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
