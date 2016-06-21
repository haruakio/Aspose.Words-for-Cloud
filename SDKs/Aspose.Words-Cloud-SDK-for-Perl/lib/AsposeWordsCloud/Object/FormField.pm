package AsposeWordsCloud::Object::FormField;

require 5.6.0;
use strict;
use warnings;
use utf8;
use JSON qw(decode_json);
use Data::Dumper;
use Module::Runtime qw(use_module);
use Log::Any qw($log);
use Date::Parse;
use DateTime;

use base "AsposeWordsCloud::Object::BaseObject";

#
#
#
#NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
#

my $swagger_types = {
    'Name' => 'string',
    'Enabled' => 'boolean',
    'StatusText' => 'string',
    'OwnStatus' => 'boolean',
    'HelpText' => 'string',
    'OwnHelp' => 'boolean',
    'CalculateOnExit' => 'boolean',
    'EntryMacro' => 'string',
    'ExitMacro' => 'string',
    'NodeId' => 'string',
    'link' => 'Link'
};

my $attribute_map = {
    'Name' => 'Name',
    'Enabled' => 'Enabled',
    'StatusText' => 'StatusText',
    'OwnStatus' => 'OwnStatus',
    'HelpText' => 'HelpText',
    'OwnHelp' => 'OwnHelp',
    'CalculateOnExit' => 'CalculateOnExit',
    'EntryMacro' => 'EntryMacro',
    'ExitMacro' => 'ExitMacro',
    'NodeId' => 'NodeId',
    'link' => 'link'
};

# new object
sub new { 
    my ($class, %args) = @_; 
    my $self = { 
        #
        'Name' => $args{'Name'}, 
        #
        'Enabled' => $args{'Enabled'}, 
        #
        'StatusText' => $args{'StatusText'}, 
        #
        'OwnStatus' => $args{'OwnStatus'}, 
        #
        'HelpText' => $args{'HelpText'}, 
        #
        'OwnHelp' => $args{'OwnHelp'}, 
        #
        'CalculateOnExit' => $args{'CalculateOnExit'}, 
        #
        'EntryMacro' => $args{'EntryMacro'}, 
        #
        'ExitMacro' => $args{'ExitMacro'}, 
        #
        'NodeId' => $args{'NodeId'}, 
        #
        'link' => $args{'link'}
    }; 

    return bless $self, $class; 
}  

# get swagger type of the attribute
sub get_swagger_types {
    return $swagger_types;
}

# get attribute mappping
sub get_attribute_map {
    return $attribute_map;
}

1;