# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopvar(RPackage):
	"""Genomic Breeding Tools: Genetic Variance Prediction and
	Cross-Validation.

	The main attribute of 'PopVar' is the prediction of genetic variance in
	bi-parental populations,  from which the package derives its name. 'PopVar'
	contains a set of functions that use phenotypic and genotypic data from a
	set of candidate parents to 1) predict the mean, genetic variance, and
	superior progeny value of all,  or a defined set of pairwise bi-parental
	crosses, and 2) perform cross-validation to estimate genome-wide prediction
	accuracy of multiple statistical models. More details are available in
	Mohammadi, Tiede, and Smith (2015, <doi:10.2135/cropsci2015.01.0030>).  A
	dataset 'think_barley.rda' is included for reference and examples."""

	cran = "PopVar"

	version("1.3.1", md5="b87f9acff8b1fc702bf4c4dfabc54795")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bglr", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
