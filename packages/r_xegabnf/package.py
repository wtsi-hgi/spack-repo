# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegabnf(RPackage):
	"""Compile a Backus-Naur Form Specification into an R Grammar
Object

	Translates a BNF (Backus-Naur Form) specification of a 
             context-free language into an R grammar object
             which consists of the start symbol, the symbol table, 
             the production table, and a short production table.
             The short production table is non-recursive. 
             The grammar object contains the file name from 
             which it was generated (without a path).
             In addition, it provides functions to determine the type 
             of a symbol (isTerminal() and isNonterminal()) and functions
             to access the production table (rules() and derives()).
             For the BNF specification, see Backus, John et al. (1962)
             "Revised Report on the Algorithmic Language ALGOL 60".
             (ALGOL60 standards page <http://www.algol60.org/2standards.htm>,
              html-edition <https://www.masswerk.at/algol60/report.htm>)
             The grammar compiler is based on the APL2 implementation in 
             Geyer-Schulz, Andreas (1997, ISBN:978-3-7908-0830-X).
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaBNF>"
	cran = "xegaBNF" 

	version("1.0.0.0", md5="a7c0269f9ae8d3d7647c755712cb98b7")

