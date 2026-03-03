# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantumops(RPackage):
	"""Performs Common Linear Algebra Operations Used in Quantum
Computing and Implements Quantum Algorithms

	Contains basic structures and operations used frequently in quantum computing. Intended to be a convenient tool to help learn quantum mechanics and algorithms. Can create arbitrarily sized kets and bras and implements quantum gates, inner products, and tensor products. Creates arbitrarily controlled versions of all gates and can simulate complete or partial measurements of kets. Has functionality to convert functions into equivalent quantum gates and model quantum noise. Includes larger applications, such as Steane error correction <DOI:10.1103/physrevlett.77.793>, Quantum Fourier Transform and Shor's algorithm (Shor 1999), Grover's algorithm (1996), Quantum Approximation Optimization Algorithm (QAOA) (Farhi, Goldstone, and Gutmann 2014) <arXiv:1411.4028>, and a variational quantum classifier (Schuld 2018) <arXiv:1804.00633>. Can be used with the gridsynth algorithm <arXiv:1212.6253> to perform decomposition into the Clifford+T set.
	"""
	
	cran = "QuantumOps" 

	version("3.0.1", md5="73cd166d31088b082d4749b40657821f")

	depends_on("r@3.1:", type=("build", "run"))
