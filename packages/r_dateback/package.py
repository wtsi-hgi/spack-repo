# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDateback(RPackage):
	"""Collect and Install R Packages on a Specified Date with
Dependencies

	Works as a virtual CRAN snapshot for source packages.
    It automatically downloads and installs 'tar.gz' files with dependencies,
    all of which were available on a specific day.
	"""
	
	homepage = "https://github.com/r-suzuki/dateback"
	cran = "dateback" 

	version("1.0.3", md5="766bf5e2c47ff30b2a2e8f0a12622e38")

