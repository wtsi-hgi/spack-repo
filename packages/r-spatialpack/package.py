# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialpack(RPackage):
	"""Tools to assess the association between two spatial processes.

	Tools to assess the association between two spatial processes. Currently,
	several methodologies are implemented: A modified t-test to perform
	hypothesis testing about the independence between the processes, a suitable
	nonparametric correlation coefficient, the codispersion coefficient, and an
	F test for assessing the multiple correlation between one spatial process
	and several others. Functions for image processing and computing the
	spatial association between images are also provided."""

	cran = "SpatialPack"

	version("0.4", md5="ce8cc05d5d3146b1b15d31740847aaf4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
