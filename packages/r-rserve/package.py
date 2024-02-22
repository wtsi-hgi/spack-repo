# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRserve(RPackage):
	"""Binary R server

	Rserve acts as a socket server (TCP/IP or local sockets) 
	     which allows binary requests to be sent to R. Every
	     connection has a separate workspace and working
	     directory. Client-side implementations are available
	     for popular languages such as C/C++ and Java, allowing
	     any application to use facilities of R without the need of
	     linking to R code. Rserve supports remote connection,
	     user authentication and file transfer. A simple R client
	     is included in this package as well.
	"""
	
	homepage = "http://www.rforge.net/Rserve/"
	cran = "Rserve" 

	version("1.8-13", md5="1ff84f0cc4c026ccec13686bd9f17846")

	depends_on("r@1.5:", type=("build", "run"))
