#!/usr/bin/env python

from os.path import join


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration("poliastro", parent_package, top_path)

    config.add_library('ast2body',
                       sources=[join('poliastro', 'fortran', '*.for')])
    config.add_library('astiod',
                       sources=[join('poliastro', 'fortran', '*.for')])

    config.add_extension('_ast2body',
                         sources=['poliastro/ast2body.pyf'],
                         libraries=['ast2body'])
    config.add_extension('_astiod',
                         sources=['poliastro/astiod.pyf'],
                         libraries=['astiod'])

    config.add_data_dir(('tests', 'poliastro/tests'))

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(version='0.0.1-dev',
          description="poliastro - Utilities and Python wrappers for"
                      "Orbital Mechanics",
          author="Juan Luis Cano",
          data_files=[('poliastro/octave', ['poliastro/octave/{}'.format(fn) for fn in
                                            ('angl.m', 'constmath.m', 'mag.m',
                                             'newtonm.m', 'newtonnu.m',
                                             'rv2coe.m', 'uplanet_2013.m')])],
          packages=['poliastro'],
          configuration=configuration)
