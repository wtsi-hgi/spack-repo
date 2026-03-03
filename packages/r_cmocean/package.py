# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmocean(RPackage):
	"""Beautiful Colour Maps for Oceanography

	Perceptually uniform palettes for commonly used
	variables in oceanography as functions taking an integer
	and producing character vectors of colours.
	See Thyng, K.M., Greene, C.A., Hetland, R.D., Zimmerle, H.M.
	and S.F. DiMarco (2016) <doi:10.5670/oceanog.2016.66> for
	the guidelines adhered to when creating the palettes.
	"""
	
	homepage = "https://matplotlib.org/cmocean/"
	cran = "cmocean" 

	version("0.3-1", md5="470eaca063a08d49c9d4a565ea4f4024")

	depends_on("r@3:", type=("build", "run"))
