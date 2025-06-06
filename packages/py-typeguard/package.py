# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTypeguard(PythonPackage):
    """
    Run-time type checker for Python.
    """

    homepage = "https://github.com/agronholm/typeguard"
    pypi = "typeguard/typeguard-2.12.1.tar.gz"

    maintainers("meyersbs")

    license("MIT")

    version("4.4.3", sha256="be72b9c85f322c20459b29060c5c099cd733d5886c4ee14297795e62b0c0d59b")
    version("4.4.2", sha256="a6f1065813e32ef365bc3b3f503af8a96f9dd4e0033a02c28c4a4983de8c6c49")
    version("4.4.1", sha256="0d22a89d00b453b47c49875f42b6601b961757541a2e1e0ef517b6e24213c21b")
    version("4.4.0", sha256="463bd8697a65a4aa576a63767c369b1ecfba8a5ba735edfe3223127b6ecfa28c")
    version("4.3.0", sha256="92ee6a0aec9135181eae6067ebd617fd9de8d75d714fb548728a4933b1dea651")
    version("4.2.1", sha256="c556a1b95948230510070ca53fa0341fb0964611bd05d598d87fb52115d65fee")
    version("4.2.0", sha256="2aeae510750fca88d0a2ceca3e86de7f71aa43b6c3e6c267737ce1f5effc4b34")
    version("4.1.5", sha256="ea0a113bbc111bcffc90789ebb215625c963411f7096a7e9062d4e4630c155fd")
    version("4.1.4", sha256="be02ad8b191eefe7abc5818f846c905f56676a3f24aa5f1a783fda17825eee9b")
    version("4.1.3", sha256="7d4264cd631ac1157c5bb5ec992281b4f1e2ba7a35db91bc15f442235e244803")
    version("4.1.2", sha256="3be187945f9ef5a9f6d7a926dfe54babb7dfd807085ce05f9a5e8735f2487990")
    version("4.1.1", sha256="278ad7a974c9e6325037751fdffc470b9b0212d282c1746ecc452235922e3602")
    version("4.1.0", sha256="b05a54bb0276eefd28880df42e004a71e699c8081fcb9d0536b2ceb01019f60c")
    version("3.0.2", sha256="fee5297fdb28f8e9efcb8142b5ee219e02375509cd77ea9d270b5af826358d5a")
    version("2.13.3", sha256="00edaa8da3a133674796cf5ea87d9f4b4c367d77476e185e80251cc13dfbb8c4")
    version("2.12.1", sha256="c2af8b9bdd7657f4bd27b45336e7930171aead796711bc4cfc99b4731bb9d051")

    depends_on("python@3.5.3:", when="@:2.13.3", type=("build", "run"))
    depends_on("python@3.7.4:", when="@3.0.2:", type=("build", "run"))
    depends_on("py-setuptools@42:", when="@:2.13.3", type="build")
    depends_on("py-setuptools@64:", when="@3.0.2:", type="build")
    depends_on("py-setuptools-scm@3.4:+toml", when="@:2.13.3", type="build")
    depends_on("py-setuptools-scm@6.4:+toml", when="@3.0.2:", type="build")
    depends_on("py-importlib-metadata@3.6:", when="@3.0.2: ^python@:3.9", type=("build", "run"))
    depends_on("py-typing-extensions@4.4.0:", when="@3.0.2: ^python@:3.10", type=("build", "run"))
