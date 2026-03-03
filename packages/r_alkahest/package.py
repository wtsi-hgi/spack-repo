# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlkahest(RPackage):
	"""Pre-Processing XY Data from Experimental Methods

	A lightweight, dependency-free toolbox for pre-processing XY
    data from experimental methods (i.e. any signal that can be measured
    along a continuous variable). This package provides methods for
    baseline estimation and correction, smoothing, normalization,
    integration and peaks detection. Baseline correction methods includes
    polynomial fitting as described in Lieber and Mahadevan-Jansen (2003)
    <doi:10.1366/000370203322554518>, Rolling Ball algorithm after Kneen
    and Annegarn (1996) <doi:10.1016/0168-583X(95)00908-6>, SNIP algorithm
    after Ryan et al. (1988) <doi:10.1016/0168-583X(88)90063-8>, 4S Peak
    Filling after Liland (2015) <doi:10.1016/j.mex.2015.02.009> and more.
	"""
	
	homepage = "https://packages.tesselle.org/alkahest/"
	cran = "alkahest" 

	version("1.1.1", md5="6cfcc3cfffb017e70d52c015c8ce230e")

	depends_on("r@3.5:", type=("build", "run"))
