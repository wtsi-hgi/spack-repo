# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyslognet(RPackage):
	"""Send Log Messages to Remote 'syslog' Server

	Send 'syslog' protocol messages to a remote 'syslog' server
    specified by host name and TCP network port.
	"""
	
	homepage = "https://github.com/philaris/syslognet"
	cran = "syslognet" 

	version("0.1.2.1", md5="387e01049d15fc12dd07a2725b138bc1")

