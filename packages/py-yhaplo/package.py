# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-yhaplo
#
# You can edit this file again by typing:
#
#     spack edit py-yhaplo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyYhaplo(PythonPackage):
    """Identifying Y-chromosome haplogroups in arbitrarily large samples of sequenced or genotyped men."""

    homepage = "https://github.com/23andMe/yhaplo"
    url = "https://github.com/23andMe/yhaplo/archive/refs/tags/2.1.13.tar.gz"

    version("2.1.13", sha256="ccd179f17afefd214b660b06abd267a728ae8b430ebb9e30a74a3ad476e44e36")
    version("2.1.10", sha256="c8003010370cc4339202a8914c5cad83058d332582a7cd89b75b95d7277f2ea4")
    version("2.1.9", sha256="2fc21373de5b09a521bb01fa9885ce9466c0658f40358c637380b9294717913f")
    version("2.1.7", sha256="5809a63031d80b378d8ed2b1268ae0974d7758dcb9b5ffc1f938e7ae5021f8a9")
    version("2.1.6", sha256="b35de73a2e87f79c7e61b4a0ffff039c38fb013208cf822a2439fdbf68fedb0b")
    version("2.1.4", sha256="718ad4dfb812cb1a25e711453f599c4c4f460fab568c0faa73eee340e1691d64")
    version("2.1.0", sha256="020f540b91e5c8feaf593b65fd289ebb06f160dea563e5b4d1112b9800190946")
    version("2.0.2", sha256="2259583adc63d1aa20c5c8c00928a6507267faf069df01b4c0e8e9fa629f9328")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    # Core dependencies
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))

