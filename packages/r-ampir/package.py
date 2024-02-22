# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpir(RPackage):
	"""Predict Antimicrobial Peptides

	A toolkit to predict antimicrobial peptides from protein sequences on a genome-wide scale.
    It incorporates two support vector machine models ("precursor" and "mature") trained on publicly available antimicrobial peptide data using calculated
    physico-chemical and compositional sequence properties described in Meher et al. (2017) <doi:10.1038/srep42362>.
    In order to support genome-wide analyses, these models are designed to accept any type of protein as input
    and calculation of compositional properties has been optimised for high-throughput use. For best results it is important to select the model that accurately 
    represents your sequence type: for full length proteins, it is recommended to use the default "precursor" model. The alternative, "mature", model is best suited
    for mature peptide sequences that represent the final antimicrobial peptide sequence after post-translational processing. For details see Fingerhut et al. (2020) <doi:10.1093/bioinformatics/btaa653>.
    The 'ampir' package is also available via a Shiny based GUI at <https://ampir.marine-omics.net/>.
	"""
	
	homepage = "https://github.com/Legana/ampir"
	cran = "ampir" 

	version("1.1.0", md5="cb7f39b1d9b1da87ecccff3675dcb2f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-peptides", type=("build", "run"))
	depends_on("r-caret@6:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
