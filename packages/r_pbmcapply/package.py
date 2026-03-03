# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbmcapply(RPackage):
	"""Tracking the Progress of Mc*pply with Progress Bar

	A light-weight package helps you track and visualize
  the progress of parallel version of vectorized R functions (mc*apply).
  Parallelization (mc.core > 1) works only on *nix (Linux, Unix such as macOS) system due to
  the lack of fork() functionality, which is essential for mc*apply, on Windows.
	"""
	
	homepage = "https://github.com/kvnkuang/pbmcapply"
	cran = "pbmcapply" 

	version("1.5.1", md5="23eabe886b2305e4790e3425d1f57e3c")

