# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransplantr(RPackage):
	"""Audit and Research Functions for Transplantation

	A set of vectorised functions to calculate medical equations used in transplantation, 
    focused mainly on transplantation of abdominal organs. These functions include donor and recipient
    risk indices as used by NHS Blood & Transplant, OPTN/UNOS and Eurotransplant, tools for 
    quantifying HLA mismatches, functions for calculating estimated glomerular filtration rate (eGFR), 
    a function to calculate the APRI (AST to platelet ratio) score used in initial screening of suitability to receive a 
    transplant from a hepatitis C seropositive donor and some biochemical unit converter functions. 
    All functions are designed to work with either US or international units.
    References for the equations are provided in the vignettes and function documentation.
	"""
	
	homepage = "https://transplantr.txtools.net"
	cran = "transplantr" 

	version("0.2.0", md5="5f14c98a102c990fa03cb01821b3ba5b")

	depends_on("r@3.1:", type=("build", "run"))
