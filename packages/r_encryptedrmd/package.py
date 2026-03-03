# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncryptedrmd(RPackage):
	"""Encrypt Html Reports Using 'Libsodium'

	Create encrypted html files that are fully self contained and do
  not require any additional software. Using the package you can encrypt
  arbitrary html files and also directly create encrypted 'rmarkdown' html reports.
	"""
	
	homepage = "https://github.com/dirkschumacher/encryptedRmd"
	cran = "encryptedRmd" 

	version("0.2.1", md5="0ccee42f682b2b1a49a35ab2d6bd39a6")

	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
