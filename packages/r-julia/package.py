# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJulia(RPackage):
	"""Fractal Image Data Generator

	Generates image data for fractals (Julia and Mandelbrot sets) on the complex plane in the given region and resolution. Benoit B Mandelbrot (1982).
	"""
	
	homepage = "https://github.com/msuzen/Julia"
	cran = "Julia" 

	version("1.3.5", md5="f0ae886ec22fd6ec62df8f072e339695")

