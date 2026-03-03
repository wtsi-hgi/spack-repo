# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaultr(RPackage):
	"""Vault Client for Secrets and Sensitive Data

	Provides an interface to a 'HashiCorp' vault server over
  its http API (typically these are self-hosted; see
  <https://www.vaultproject.io>).  This allows for secure storage and
  retrieval of secrets over a network, such as tokens, passwords and
  certificates.  Authentication with vault is supported through
  several backends including user name/password and authentication via
  'GitHub'.
	"""
	
	homepage = "https://github.com/vimc/vaultr"
	cran = "vaultr" 

	version("1.2.0", md5="95459e9b7392558892fcd2f4f75a062d")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
