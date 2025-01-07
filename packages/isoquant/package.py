# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from os import chmod

from spack.package import *


class Isoquant(Package):
    """IsoQuant is a tool for the genome-based analysis of long RNA reads, such as PacBio or Oxford Nanopores. IsoQuant allows to reconstruct and quantify transcript models with high precision and decent recall. If the reference annotation is given, IsoQuant also assigns reads to the annotated isoforms based on their intron and exon structure. IsoQuant further performs annotated gene, isoform, exon and intron quantification. If reads are grouped (e.g. according to cell type), counts are reported according to the provided grouping."""

    homepage = "https://github.com/ablab/IsoQuant"
    url = "https://github.com/ablab/IsoQuant/archive/refs/tags/v3.5.2.tar.gz"

    version("3.6.2", sha256="7d620cdf4055a55132d6c66b45b706172cd5aae71bc91ac48e409311e8cc1530")
    version("3.6.1", sha256="5e55749b0e7694382892929b283979bf513ee30e4c405c8ee9ddc1e40032f7dd")
    version("3.5.2", sha256="cad3d8df81324fd4a857c2ad8057c6207cb66f422f90afe36337aa95d4135951")
    version("3.5.1", sha256="1840c6a7224951bf4084f840201c42628c439c0d0404f12d47734eec403f8179")
    version("3.5.0", sha256="8cbba80b5eb0ed85fe0b519693157eb97820bc1d79ff44435736bf799af85c1f")
    version("3.4.2", sha256="7e620dc1aaffecc19155137c6766e47b3fea07822626bd2a23e7b8e57ffac18f")
    version("3.4.1", sha256="df30e662730071908c8f048037ca93821ac6c62a963aaaa9da783bf341871d60")
    version("3.4.0", sha256="19fb81cc97b3d65fecbd996e099d2a906c894de3984e5bc7b99852887696b171")
    version("3.3.1", sha256="5b6f47f46eb95254f5df1c3f1ba113361011adeada4396f680f5e456460d02f2")
    version("3.3.0", sha256="5c0e793a33f1b39b9f4888f7bade7f827f68bfb113535e08099906f7ad4689ce")
    version("3.2.0", sha256="8286b9d65bc2d755b742766ca8e0d0b86443ff2246dab6e68c213d54b4ede67c")
    version("3.1.2", sha256="7a0175cfb613485c1ea405457677eb6660a99b6aa794fd2e84fa72ed738cab92")

    depends_on("samtools", type="run")
    depends_on("minimap2", type="run")
    depends_on("py-gffutils@0.10.1:", type="run")
    depends_on("py-biopython@1.76:", type="run")
    depends_on("py-pandas@1.0.1:", type="run")
    depends_on("py-pybedtools@0.8.1:", type="run")
    depends_on("py-pysam@0.15:", type="run")
    depends_on("py-packaging", type="run")
    depends_on("py-pyfaidx@0.7:", type="run")
    depends_on("py-pyyaml@5.4:", type="run")
    depends_on("py-matplotlib@3.3.1:", type="run")
    depends_on("py-numpy@1.18.1:", type="run")
    depends_on("py-scipy@1.4.1:", type="run")
    depends_on("py-seaborn@0.10.0:", type="run")

    def install(self, spec, prefix):
        mkdir(prefix.opt)
        mkdir(prefix.opt.isoquant)
        mkdir(prefix.bin)

        install_tree(".", prefix.opt.isoquant)

        script = prefix.bin + "/isoquant.py"

        with open(script, "w") as f:
            f.write(
                '#!/bin/bash\nPYTHONPATH="$PYTHONPATH:'
                + prefix
                + '/opt/isoquant" python3 '
                + prefix
                + '/opt/isoquant/isoquant.py "$@"'
            )

        chmod(script, 755)
