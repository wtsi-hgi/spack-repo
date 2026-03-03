# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSherlockholmes(RPackage):
	"""Building a Concordance of Terms in a Series of Texts

	Compute the frequency distribution of a search term in a series of texts. For example, Arthur Conan Doyle wrote a total of 60 Sherlock Holmes stories, comprised of 54 short stories and 4 longer novels. I wanted to test my own subjective impression that, in many of the stories, Sherlock Holmes' popularity was used as bait to induce the reader to read a story that is essentially not primarily a Sherlock Holmes story. I used the term "Holmes" as a search pattern, since Watson would frequently address him by name, or use his name to describe something that he was doing. My hypothesis is that the frequency distribution of the search pattern "Holmes" is a good proxy for the degree to which a story is or is not truly a Sherlock Holmes story. The results are presented in a manuscript that is available as a vignette and online at <https://barryzee.github.io/Concordance/index.html>.
	"""
	
	cran = "SherlockHolmes" 

	version("1.0.1", md5="42ec296b11b66c65f1e9f767c67217f7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dpseg", type=("build", "run"))
	depends_on("r-tablehtml", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
	depends_on("r-textboxplacement", type=("build", "run"))
	depends_on("r-plot-matrix", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
