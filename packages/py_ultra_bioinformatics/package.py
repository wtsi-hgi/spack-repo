# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUltraBioinformatics(PythonPackage):
    """Splice aligner of long transcriptomic reads to genome."""

    homepage = "https://github.com/ksahlin/uLTRA"
    pypi = "ultra-bioinformatics/ultra_bioinformatics-0.1.tar.gz"

    version("0.0.1", sha256="a4e61a998acdde447ba08aa6e43845ac44e27466e38032739c016a6f29972b2a")
    version("0.0.2", sha256="fa4c15927e73e25d98ce7884765ce5af26986cd646a1162d840d9e019cbd66e3")
    version("0.0.2.1", sha256="4efc237f9759fe47808c22c1ee564412edf39c3dc21b0aa6b2af74009d2d64a7")
    version("0.0.2.2", sha256="7557c1f0137b290c24bbf5a3255f028c5c26ab03aa14264d0cf7aa0a20499818")
    version("0.0.2.3", sha256="a9686a3fafee9539aff6728667008e892f4a5acdf9558edfb48b7f2fdf8fc2b4")
    version("0.0.2.4", sha256="953e1dcad9bcec9c461e9b6492cfb2b76d907859a313c38764d20a9e6dca49b9")
    version("0.0.3", sha256="7589ed76616a5ff9c8a37acc472d909e971fd94d32abf8bab84c4b7a369b935f")
    version("0.0.3.1", sha256="589cc94b3b3e7aced842232bb7781734892ef7887fdfe6d1209f2f17a4e5016d")
    version("0.0.3.2", sha256="33b22d9edbc46914c8eef360dbdc1db647a7b49f3ebc221342adee0da0d4a4d4")
    version("0.0.3.3", sha256="55bb09883955f2619e9e7f1653901409c71091e5e068100c549913be43bbd043")
    version("0.0.4", sha256="aa098f808330d42d55bc44f73fc2f1f3b0b44487c04062f82df6c2b42d996598")
    version("0.0.4.1", sha256="30730c868918fb22eba7fbe5df09d514cf9ffff69e29777cfdd36d06d22c6ddf")
    version("0.0.4.2", sha256="5ff4169a7090737e61f4a257468fc1f7d523d97d7ab418d155ad685f8676da1d")
    version("0.1", sha256="c477b526cba52fcaf369efb67f0d0096ea1702d7adc8457746a91ae5f750a0ef")

    depends_on("py-setuptools", type=("build"))
    depends_on("namfinder", type=("build", "run"))
    depends_on("minimap2", type=("build", "run"))
