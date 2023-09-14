# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParameters(RPackage):
    """Utilities for processing the parameters of various statistical models."""

    homepage = "https://easystats.github.io/parameters/"
    cran = "parameters"

    version("0.21.1", sha256="70a6d6f4b9dd7f4ec022c9860dd24d9a2852d87ccf77721e0e336b733040b3ed")
    version("0.21.0", sha256="4658b47bdedbfda381ce1b7493ee1cb0f27fa3264a7f6cf0557063f123d142a4")
    version("0.20.3", sha256="b3ddcaa8ded56b04af8d3371acf638dd17ad5f49726b6bbf9d014c7c0b6738b2")
    version("0.20.2", sha256="c8a6097362e02c503539f960a16a91deebf582c9aaeaf7115dd78f458bb2f8a4")
    version("0.20.1", sha256="53435152750c54eae7a10734f7a62f3a56cb544b52eddd92a52fe42f50396ff7")
    version("0.20.0", sha256="37d1141baa0fe347bad58dc1d53bbd8802be5b6d99b5d70fc3baa0010916c99b")
    version("0.19.0", sha256="ae0a36dcbafc9e977ac418731890edfd5904bd0f24cf898dcf9659c9de469481")
    version("0.18.2", sha256="e92b504adaf9a907a993233d1c9b58144fed53d82439caaa1d9e8cf553785c13")
    version("0.18.1", sha256="e929c46bc29eab7ed17e61b3cd6e9d13fe98f0e80fdf8d82ba859ce886bb9e7d")
    version("0.18.0", sha256="9067a92576027f08a687f3bc6341f8081a6d27ba80c7cdcad91ec3ec9290cb64")
    version("0.17.0", sha256="e94089accb80951dceff94d9d28fb381647369d6963cf8582044980cf3d03073")
    version("0.16.0", sha256="475020d997aceb121a83178582d1b1c9f7ac55e4a9fc9deebe234b6c4b2b49c4")
    version("0.15.0", sha256="742ea02447346ac943a28b5122934293cbd01dbda87fdca06f1dbcc0285f0638")
    version("0.14.0", sha256="c7349620fdf8a43e9dee93ecfb744cca889a126c4681580466e9dff52382a20f")
    version("0.13.0", sha256="01e110add2237076971c63d77197d3c4696e3588b25b126814dfd00c53e7b49d")
    version("0.12.0", sha256="f5560a97287cad3a5c6e2bc7f834a8edcf6729f45009b55be597564c28b1d835")
    version("0.11.0", sha256="0c2f0821c11af21246e2bf7f443824873cb5c190bbf4ce26cd72836bfb1e1308")
    version("0.10.1", sha256="e81c2a0350a54051cb4dc9808b8b9c12f977b80d54ece312101443d09ade72f7")
    version("0.10.0", sha256="bab5a8462875e59a107614737653a9011b1a2773cef1f560dfb5e8b40f501c89")
    version("0.9.0", sha256="2633e35452994be6505cf9768951d681da42a8aa9067ad76a345748b83af529e")
    version("0.8.6", sha256="dc0430eb9d95f20ca0985152bc5eba496b1118adbef973e2d396c77e85f1987c")
    version("0.8.5", sha256="9420011b9a78047413e95d90144e375d589b1724c144a1e76a4d60fbc32d5ded")
    version("0.8.2", sha256="b0ae75ef23eef4e35ee603e708ebd5e7167d54adb5d0191f816d73cff4d7554d")
    version("0.8.0", sha256="5d61a5b450e6c2fa36f7192ffb75d146ffc92885dfa02255ea0d13671814abb2")
    version("0.7.0", sha256="4578360c4c5daca25b816d1ec2a76bc265669f915e833957f4122e70b45d9907")
    version("0.6.1", sha256="be990a9437505b18dc724c6ae52e008811a70508fd1466dc24b31a1fdcecd457")
    version("0.6.0", sha256="b6072232e23c57f0894883c11db8b3a40e065703fa173bc2617004c0661c367e")
    version("0.5.0", sha256="27cba754e0e5e5e0d83c9552e1000f57afa65de1333e3e64b95ba70370a68ba5")
    version("0.4.1", sha256="71353c8e947feef3010cc90ddd2d7c8b285663b2f50706fd9b26eb7440b06d76")
    version("0.4.0", sha256="a6358ce76580b0786ddf45f6cea7f2732641cd5fab2388848c90dd1b5f6f307c")
    version("0.3.0", sha256="bbf1a2e3f0c072784faf8bfb523d6bfda132e9432d39797030c66a04c34bcb45")
    version("0.2.0", sha256="f0717573f2932f1efd28a54d15c0c48937a11727c813cc58948f1f43c77aefd5")
    version("0.1.0", sha256="e5a1c9799fd0e77c6306cfc9b52893bed26e150113b8c562f37dd0a07600638b")

    depends_on("r-bayestestr", type=("build", "run"))
    depends_on("r-datawizard", type=("build", "run"))
    depends_on("r-insight@0.19.2:", type=("build", "run"))
