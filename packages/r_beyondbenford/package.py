# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeyondbenford(RPackage):
	"""Compare the Goodness of Fit of Benford's and Blondeau Da Silva's
Digit Distributions to a Given Dataset

	Allows to compare the goodness of fit of Benford's and Blondeau Da Silva's digit distributions in a dataset. It is used to check whether the data distribution is consistent with theoretical distributions highlighted by Blondeau Da Silva or not (through the dat.distr() function): this ideal theoretical distribution must be at least approximately followed by the data for the use of Blondeau Da Silva's model to be well-founded. It also enables to plot histograms of digit distributions, both observed in the dataset and given by the two theoretical approaches (with the digit.ditr() function). Finally, it proposes to quantify the goodness of fit via Pearson's chi-squared test (with the chi2() function).
	"""
	
	cran = "BeyondBenford" 

	version("1.4", md5="a761dc896448643d91f7f27de529fd23")

	depends_on("r-ggplot2@2.1:", type=("build", "run"))
