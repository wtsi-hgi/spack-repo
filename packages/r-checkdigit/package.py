# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckdigit(RPackage):
	"""Calculate and Verify Check Digits

	Check digits are used like file hashes to verify that a
    number has been transcribed accurately. The functions provided by this
    package help to calculate and verify check digits according to various
    algorithms.
	"""
	
	homepage = "https://fascinatingfingers.gitlab.io/checkdigit"
	cran = "CheckDigit" 

	version("1.0.0", md5="fd2fa8b775436fc0af9ca6f89e3a1f6c")

