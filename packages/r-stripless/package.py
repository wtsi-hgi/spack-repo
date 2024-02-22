# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStripless(RPackage):
	"""Structured Trellis Displays Without Strips for Lattice Graphics

	For making Trellis-type conditioning plots without strip labels.
    This is useful for displaying the structure of results from factorial designs
    and other studies when many conditioning variables would clutter the display
    with layers of redundant strip labels. Settings of the variables are encoded by
    layout and spacing in the trellis array and decoded by a separate legend. The
    functionality is implemented by a single S3 generic strucplot() function that
    is a wrapper for the Lattice package's xyplot() function. This allows access to
    all Lattice graphics capabilities in the usual way.
	"""
	
	cran = "stripless" 

	version("1.0-3", md5="9ed2e96dd788e6dc4cb490db0031cc31")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
