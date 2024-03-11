# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Finemap(Package):
    """In genomic regions associated with complex traits and disease. FINEMAP is computationally efficient by using summary statistics from genome-wide association studies and robust by applying a shotgun stochastic search algorithm (Hans et al., 2007). It produces accurate results in a fraction of processing time of existing approaches. It is therefore the ideal tool for analyzing growing amounts of data produced in genome-wide association studies and emerging sequencing or biobank projects."""

    homepage = "http://www.christianbenner.com/"
    url = "http://www.christianbenner.com/finemap_v1.4.2_x86_64.tgz"

    version("1.4.2", sha256="3b1fc6eb3c2ccafd647b32e02d0244495cd0ade9ed7d474606c31ebf6e98b0c9")
    version("1.4.1", sha256="75c919d9cc981bc08e1a982b1632110109ffe6a057e803c9aa36c143aa56d546")
    version("1.4", sha256="4a70e25317a314b07890c54be2f8acfd0d3dd64aa456941f06464867a4a547aa")
    version("1.3.1", sha256="7050e56087ea8677dc69e1db71e572f380a0200ae698ba343840726edbd6cac9")
    version("1.3", sha256="d405f2bba77128af5916f0650de12dd4da80fd570a896d82178a498057758aac")
    version("1.2", sha256="aaaa59c9e9bfcf5705a0c3704aaa0dedde0467f66f80469d3e759611dea0fa0d")
    version("1.1", sha256="3a6ea6bbe86a9607b4b01f0db0a700d24068af96ed597e70cab390cf12def787")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("finemap_v1.4.2_x86_64", prefix.bin)
