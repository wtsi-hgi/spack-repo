# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspm(RPackage):
	"""'RStudio' Package Manager

	Enables binary package installations on Linux distributions.
    Provides access to 'RStudio' public repositories at
    <https://packagemanager.posit.co>, and transparent management of
    system requirements without administrative privileges. Currently supported
    distributions are 'CentOS' / 'RHEL' 7-9, and several 'RHEL' derivatives
    ('Rocky Linux', 'AlmaLinux', 'Oracle Linux', and 'Amazon Linux' 2),
    'openSUSE' / 'SLES' 15.3-4, 'Debian' 11-12, and 'Ubuntu' LTS 18-22.
	"""
	
	homepage = "https://cran4linux.github.io/rspm/"
	cran = "rspm" 

	version("0.5.0", md5="a4eb09ed4f2b193c186a3f78f9525c23")

