# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncryptr(RPackage):
	"""Easily Encrypt and Decrypt Data Frame/Tibble Columns or Files
using RSA Public/Private Keys

	It is important to ensure that sensitive data is protected. 
    This straightforward package is aimed at the end-user. 
    Strong RSA encryption using a public/private key pair is used to encrypt data frame or tibble columns.
    A public key can be shared to allow others to encrypt data to be sent to you. 
    This is particularly aimed a healthcare settings so patient data can be pseudonymised. 
	"""
	
	homepage = "https://github.com/SurgicalInformatics/encryptr"
	cran = "encryptr" 

	version("0.1.3", md5="f79a852feb7dfab88669b2a7c7629fcc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
