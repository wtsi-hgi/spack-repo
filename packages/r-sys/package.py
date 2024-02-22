# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSys(RPackage):
	"""Powerful and Reliable Tools for Running System Commands in R.

	Drop-in replacements for the base system2() function with fine control and
	consistent behavior across platforms. Supports clean interruption, timeout,
	background tasks, and streaming STDIN / STDOUT / STDERR over binary or text
	connections. Arguments on Windows automatically get encoded and quoted to
	work on different locales."""

	cran = "sys"

	version("3.4.2", md5="79b75f8ec16557df22600458b6044ebe")


	def flag_handler(self, name, flags):
		if name == "cflags":
			flags.append(self.compiler.c99_flag)
		return (flags, None, None)
