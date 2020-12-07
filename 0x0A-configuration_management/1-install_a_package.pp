#installs puppet lint

package {'puppet-lint (2.1.1)':
  ensure   => 'installed',
  provider => 'gem',
}
