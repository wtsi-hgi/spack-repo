# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmentr(RPackage):
	"""Segment Data With Maximum Likelihood

	Given a likelihood provided by the user, this package applies it
    to a given matrix dataset in order to find change points in the data that
    maximize the sum of the likelihoods of all the segments. This package provides
    a handful of algorithms with different time complexities and assumption compromises
    so the user is able to choose the best one for the problem at hand. The implementation
    of the segmentation algorithms in this package are based on the paper by Bruno M. de Castro,
	Florencia Leonardi (2018) <arXiv:1501.01756>. The Berlin
	weather sample dataset was provided by Deutscher Wetterdienst <https://dwd.de/>.
	You can find all the references in the Acknowledgments section of this package's
	repository via the URL below.
	"""
	
	homepage = "https://github.com/thalesmello/segmentr"
	cran = "segmentr" 

	version("0.2.0", md5="27f4aa3d06f62e4dcc54386eeed24ec8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
