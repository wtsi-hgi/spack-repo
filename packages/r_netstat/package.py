# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetstat(RPackage):
	"""Retrieve Network Statistics Including Available TCP Ports

	R interface for the 'netstat' command line utility used to retrieve and parse 
    commonly used network statistics, including available and in-use 
    transmission control protocol (TCP) ports. Primers offering technical background information 
    on the 'netstat' command line utility are available in the "Linux System Administrator's Manual" 
    by Michael Kerrisk (2014) 
    <https://man7.org/linux/man-pages/man8/netstat.8.html>, and on the Microsoft website (2017) 
    <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/netstat>.
	"""
	
	homepage = "https://github.com/stevecondylios/netstat"
	cran = "netstat" 

	version("0.1.2", md5="14b3f2fdf863be3afd23f5de4e23de1c")

