# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMole(RPackage):
	"""Modeling Language Evolution

	Model for simulating language evolution in terms of cultural evolution (Smith & Kirby (2008) <DOI:10.1098/rstb.2008.0145>; Deacon 1997). The focus is on the emergence of argument-marking systems (Dowty (1991) <DOI:10.1353/lan.1991.0021>, Van Valin 1999, Dryer 2002, Lestrade 2015a), i.e. noun marking (Aristar (1997) <DOI:10.1075/sl.21.2.04ari>, Lestrade (2010) <DOI:10.7282/T3ZG6R4S>), person indexing (Ariel 1999, Dahl (2000) <DOI:10.1075/fol.7.1.03dah>, Bhat 2004), and word order (Dryer 2013), but extensions are foreseen. Agents start out with a protolanguage (a language without grammar; Bickerton (1981) <DOI:10.17169/langsci.b91.109>, Jackendoff 2002, Arbib (2015) <DOI:10.1002/9781118346136.ch27>) and interact through language games (Steels 1997). Over time, grammatical constructions emerge that may or may not become obligatory (for which the tolerance principle is assumed; Yang 2016). Throughout the simulation, uniformitarianism of principles is assumed (Hopper (1987) <DOI:10.3765/bls.v13i0.1834>, Givon (1995) <DOI:10.1075/z.74>, Croft (2000), Saffran (2001) <DOI:10.1111/1467-8721.01243>, Heine & Kuteva 2007), in which maximal psychological validity is aimed at (Grice (1975) <DOI:10.1057/9780230005853_5>, Levelt 1989, Gaerdenfors 2000) and language representation is usage based (Tomasello 2003, Bybee 2010). In Lestrade (2015b) <DOI:10.15496/publikation-8640>, Lestrade (2015c) <DOI:10.1075/avt.32.08les>, and Lestrade (2016) <DOI:10.17617/2.2248195>), which reported on the results of preliminary versions, this package was announced as WDWTW (for who does what to whom), but for reasons of pronunciation and generalization the title was changed.
	"""
	
	cran = "MoLE" 

	version("1.0.1", md5="3f85433e12333a1cfeed140209132380")

	depends_on("r@3:", type=("build", "run"))
