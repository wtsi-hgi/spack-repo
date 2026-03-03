# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerial(RPackage):
	"""The Serial Interface Package

	Enables reading and writing binary and ASCII data to 
             RS232/RS422/RS485 or any other virtual serial interface of the
             computer.
	"""
	
	cran = "serial" 

	version("3.0", md5="99848db182c31ac8070c93e4ac81e413")

	depends_on("r@2.15:", type=("build", "run"))
