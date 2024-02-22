# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFwb(RPackage):
	"""Fractional Weighted Bootstrap

	An implementation of the fractional weighted bootstrap to be used as a drop-in for functions in
   the 'boot' package. The fractional weighted bootstrap (also known as the Bayesian bootstrap) involves drawing
   weights randomly that are applied to the data rather than resampling units from the data. See Xu et al. (2020)
   <doi:10.1080/00031305.2020.1731599> for details.
	"""
	
	homepage = "https://github.com/ngreifer/fwb"
	cran = "fwb" 

	version("0.2.0", md5="f53a73f8d658340d578e29b858c41239")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
