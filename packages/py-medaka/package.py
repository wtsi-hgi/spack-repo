# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMedaka(PythonPackage):
    """medaka is a tool to create consensus sequences and variant calls from
    nanopore sequencing data. This task is performed using neural networks
    applied a pileup of individual sequencing reads against a draft assembly.
    It provides state-of-the-art results outperforming sequence-graph based
    methods and signal-based methods, whilst also being faster."""

    homepage = "https://github.com/nanoporetech/medaka"
    pypi = "medaka/medaka-1.7.2.tar.gz"

    license("MPL-2.0")

    version("1.12.1", sha256="df4baf7d1e9154de85229aef237919619ff6ae7f7d103abb0828e449ff977adf")
    version("1.12.0", sha256="039219204111a8114b1f72d87d0d3463e43473790cff4520c8afbd79cc8784d6")
    version("1.11.3", sha256="940568212d152f573270967b02f6e841561cc43138b6aa15783c371457fef7b9")
    version("1.11.2", sha256="8dcb9941ead369b0a8715db80a3375b50a1ad8b58ea12009222b1d70f39cfb07")
    version("1.11.1", sha256="4440762a17ddd66806ddbd7c3218140caa234b96a8c919ed54d7243d3e4a5dd1")
    version("1.11.0", sha256="a763d3eb35a3fcee97012ac92357f7ff9cefe3bf7511020152bd2bb1faeb4b1d")
    version("1.10.0", sha256="864b6303b0b262e5e81acba7b0da003420906db123a5072adc82458d650a8b70")
    version("1.9.1", sha256="1018c07267d24cb4607ae823ced01a1789939b5f8143d1c240ce243dc1160ef5")
    version("1.8.2", sha256="73e5669447c4b3a948da02d64cf6d416a64c303a6938d20607c17b3dd9f25241")
    version("1.7.3", sha256="6caa50193b85d71a9ba00ac3192e13ec3193202bed6fbc216fc22781da9dc3e4")

    depends_on("python@3.6:3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-cffi@1.15.0", type=("build", "run"))
    depends_on("py-edlib", type=("build", "run"))
    depends_on("py-grpcio", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-intervaltree", type=("build", "run"))
    depends_on("py-tensorflow@2.7.0:2.7", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("minimap2", type=("build", "run"))
    depends_on("py-ont-fast5-api", type=("build", "run"))
    depends_on("py-parasail", when="target=x86_64:", type=("build", "run"))
    depends_on("py-parasail", when="target=ppc64le:", type=("build", "run"))
    depends_on("py-pysam@0.16.0.1:", type=("build", "run"))
    depends_on("py-pyspoa@0.0.3:", when="target=x86_64:", type=("build", "run"))
    depends_on("py-pyspoa@0.0.3:", when="target=ppc64le:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("samtools", type=("build", "run"))
    depends_on("htslib", type=("build", "run", "link"))

    def patch(self):
        filter_file("'build_ext': HTSBuild", "", "setup.py", string=True)
        filter_file(
            "libraries=['m', 'z', 'lzma', 'bz2', 'pthread', 'curl', 'crypto']",
            "libraries=['hts', 'm', 'z', 'lzma', 'bz2', 'pthread', 'curl', 'crypto']",
            "build.py",
            string=True,
        )
        filter_file("extra_objects=['libhts.a']", "", "build.py", string=True)
