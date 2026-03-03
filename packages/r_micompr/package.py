# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicompr(RPackage):
	"""Multivariate Independent Comparison of Observations

	A procedure for comparing multivariate samples associated with
    different groups. It uses principal component analysis to convert
    multivariate observations into a set of linearly uncorrelated statistical
    measures, which are then compared using a number of statistical methods. The
    procedure is independent of the distributional properties of samples and
    automatically selects features that best explain their differences, avoiding
    manual selection of specific points or summary statistics. It is appropriate
    for comparing samples of time series, images, spectrometric measures or
    similar multivariate observations. This package is described in Fachada et
    al. (2016) <doi:10.32614/RJ-2016-055>.
	"""
	
	homepage = "https://github.com/nunofachada/micompr"
	cran = "micompr" 

	version("1.1.4", md5="b7514730c8ef97bb16954d3eb92eb6e9")

	depends_on("r@4.1:", type=("build", "run"))
