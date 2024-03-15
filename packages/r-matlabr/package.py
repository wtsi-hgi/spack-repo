# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatlabr(RPackage):
	"""An Interface for MATLAB using System Calls

	Provides users to call MATLAB from using the "system" command.
    Allows users to submit lines of code or MATLAB m files.
    This is in comparison to 'R.matlab', which creates a MATLAB server.
	"""
	
	cran = "matlabr" 

	version("1.5.2", md5="aa8fa07a0dd59c2af93e3ce6bf4974fa")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("matlab", type=("build", "link", "run"))
