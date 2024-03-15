# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrates(RPackage):
	"""Grouped Date Classes

	Provides a coherent interface and implementation for creating
    grouped date classes. This package is part of the RECON
    (<https://www.repidemicsconsortium.org/>) toolkit for outbreak analysis.
	"""
	
	homepage = "https://www.reconverse.org/grates/"
	cran = "grates" 

	version("1.2.0", md5="14dfc9844db472917afa1d052883dec1")

