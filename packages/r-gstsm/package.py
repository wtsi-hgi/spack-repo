# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGstsm(RPackage):
	"""Generalized Spatial-Time Sequence Miner

	Implementations of the algorithms present article 
    Generalized Spatial-Time Sequence Miner, original title
    (Castro, Antonio; Borges, Heraldo ; Pacitti, Esther ; Porto, Fabio
    ; Coutinho, Rafaelli ; Ogasawara, Eduardo . Generalização de Mineração de
    Sequências Restritas no Espaço e no Tempo. In: XXXVI SBBD -
    Simpósio Brasileiro de Banco de Dados, 2021 <doi:10.5753/sbbd.2021.17891>).
	"""
	
	cran = "gstsm" 

	version("1.0.0", md5="bccde85814fe950956034e80bf069d6c")

	depends_on("r-digest", type=("build", "run"))
