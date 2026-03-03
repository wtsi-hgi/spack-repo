# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabstatr(RPackage):
	"""Libreria Del Laboratorio Di Statistica Con R

	Insieme di funzioni di supporto al volume "Laboratorio di
        Statistica con R", Iacus-Masarotto, MacGraw-Hill Italia, 2006.
        This package contains sets of functions defined in "Laboratorio
        di Statistica con R", Iacus-Masarotto, MacGraw-Hill Italia,
        2006. Function names and docs are in italian as well.
	"""
	
	cran = "labstatR" 

	version("1.0.13", md5="2c4e0a696cb0fe84a0565153f20df999")

	depends_on("r@2.10:", type=("build", "run"))
