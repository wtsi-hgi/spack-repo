# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStylest2(RPackage):
	"""Estimating Speakers of Texts

	Estimates the authors or speakers of texts. Methods developed in Huang, Perry, and Spirling (2020) <doi:10.1017/pan.2019.49>. The model is built on a Bayesian framework in which the distinctiveness of each speaker is defined by how different, on average, the speaker's terms are to everyone else in the corpus of texts. An optional cross-validation method is implemented to select the subset of terms that generate the most accurate speaker predictions. Once a set of terms is selected, the model can be estimated. Speaker distinctiveness and term influence can be recovered from parameters in the model using package functions. Once fitted, the model can be used to predict authorship of new texts.
	"""
	
	cran = "stylest2" 

	version("0.1", md5="518484b06b26e599795a052f28a4064e", url="https://cran.r-project.org/src/contrib/stylest2_0.1.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
