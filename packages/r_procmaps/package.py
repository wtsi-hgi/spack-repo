# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcmaps(RPackage):
	"""Portable Address Space Mapping

	Portable '/proc/self/maps' as a data frame.
    Determine which library or other region is mapped to a specific
    address of a process. --
    R packages can contain native code, compiled to shared libraries at build or
    installation time.
    When loaded, each shared library occupies a portion of the address space of
    the main process.
    When only a machine instruction pointer is available (e.g. from a backtrace
    during error inspection or profiling), the address space map determines
    which library this instruction pointer corresponds to.
	"""
	
	homepage = "https://r-prof.github.io/procmaps/"
	cran = "procmaps" 

	version("0.0.5", md5="0cb9845fe88df00a046d71c740ac3b34")

