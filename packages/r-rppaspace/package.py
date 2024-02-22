# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRppaspace(RPackage):
	"""Reverse-Phase Protein Array Super Position and Concentration
Evaluation

	Provides tools for the analysis of reverse-phase protein arrays (RPPAs), which are also known as 'tissue lysate arrays' or simply 'lysate arrays'. The package's primary purpose is to input a set of quantification files representing dilution series of samples and control points taken from scanned RPPA slides and determine a relative log concentration value for each valid dilution series present in each slide and provide graphical visualization of the input and output data and their relationships. Other optional features include generation of quality control scores for judging the quality of the input data, spatial adjustment of sample points based on controls added to the slides, and various types of normalization of calculated values across a set of slides. The package was derived from a previous package named SuperCurve. For a detailed description of data inputs and outputs, usage  information, and a list of related papers describing methods used in the package please review the vignette 'Guide_to_RPPASPACE'. 'RPPA SPACE: an R package for normalization and quantitation of Reverse-Phase Protein Array data'. Bioinformatics Nov 15;38(22):5131-5133. <doi: 10.1093/bioinformatics/btac665>.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/36205581"
	cran = "RPPASPACE" 

	version("1.0.10", md5="ea51240ee860ef7c2fc42e665a257f7b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-bmp", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
